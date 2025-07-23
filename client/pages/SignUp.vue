<template>
    <div class="left-[15%] signup">
        <h3>SIGN UP</h3>
        <form @submit.prevent="signup">
            <p>Choose a role:</p>
            <select name="roles" v-model="role" required placeholder="Choose a role">
                <option 
                    value="(1, user)" 
                    title="USER: This role is the basic role with minimal previleges. *NOTE: This role CANNOT create quizzes.">
                    user
                </option>
                <option 
                    value="(2, supervisor)" 
                    title="SUPERVISOR: This role is an advanced role with similar features as the USER. *NOTE: This role CAN create quizzes">
                    supervisor
                </option>
            </select>
            <br>
            <input name="email" placeholder="Enter an email" type="email" required v-model="email"></input>
            <p v-if="emailExists" class="password-error italic underline text-red-600 bg-red-300 text-xs">
                Please try again. This email has already been used before.
            </p>
            <br>
            <input name="username" placeholder="Enter a username" type="text" required v-model="username"></input>
            <p v-if="usernameExists" class="password-error italic underline text-red-600 bg-red-300 text-xs">
                Please try again. This username has already been taken.
            </p>
            <br>
            <input name="password" placeholder="Enter a password" type="password" required v-model="password"></input>
            <br>
            <input name="password" placeholder="Reenter your password" type="password" required v-model="check"></input>
            <p v-if="(check.length > 0) && (check !== password)" class="password-error italic underline text-red-600 bg-red-300 text-xs">
                Please try again. The passwords do NOT match one another.
            </p>
            <br>
            <button type="submit">Sign Up</button>
        </form>
        <br>
        <NuxtLink to="/signin">
            <p class="italic underline hover:text-sky-600">Have an account? Click here to sign in.</p>
        </NuxtLink>
    </div>
</template>

<script setup lang="ts">
const email = ref("");
const username = ref("");
const password = ref("");
const check = ref("");
const role = ref("");

const userInfo = reactive<User>({
    email: "",
    id: 0,
    role: "",
    username: "",
    accessToken: "",
    refreshToken: "",
});

const emailExists = ref(false);
const usernameExists = ref(false);

async function signup() {
    if (check.value !== password.value) {
        alert("Passwords do not match. Please try again.");
        return;
    }

    const existing = await fetchEndpoint<any[]>('/users/') || [];
    console.log(email.value, username.value, existing);
    for (const user of existing) {
        console.log(user);
        if (user.email === email.value) {
            return emailExists.value = true;
        }
        if (user.username === username.value) {
            return usernameExists.value = true;
        }
    }

    const createdUser = await fetchEndpoint<User>('/users/', 'POST', {
        email: email.value,
        username: username.value,
        password: password.value,
        role: role.value.split(',')[1].trim(), // Extract the role from the value
    });
}
</script>