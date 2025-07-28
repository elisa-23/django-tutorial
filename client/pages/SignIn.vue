<template>
    <div class="left-[15%] signin">
        <h3>SIGN IN</h3>
        <form @submit.prevent="signin">
            <input name="email" placeholder="Enter your email" type="email" required v-model="email"></input>
            <input name="password" placeholder="Enter your password" type="password" required v-model="password"></input>
            <br>
            <button type="submit">Sign In</button>
        </form>
        <br>
        <NuxtLink to="/signup">
            <p class="italic underline hover:text-sky-600">Don't have an account? Click here to sign up.</p>
        </NuxtLink>
    </div>
</template>

<script setup lang="ts">

const email = ref('');
const password = ref('');

//const config = useRuntimeConfig();       // base url access = config.public.apiBase
//Just put inside of utils!!        //will use in multi files

onBeforeMount(() => {
    email.value = '';
    password.value = '';
})

const userInfo = reactive<User>({
    email: "",
    id: 0,
    role: "",
    username: "",
    accessToken: "",
    refreshToken: "",
});

/**
 * Signs in a user using the provided email and password.
 * If the email and password are valid, the user info is stored in the userInfo reactive object.
 * The user info contains the user's id, username, email, role, access token, and refresh token.
 * If the email and password are not valid, an alert will pop up with the message "Invalid email or password. Please try again.".
 */

const userStore = useUserStore();
async function signin() {
    await userStore.signIn(email.value, password.value, userInfo);
    email.value = "";
    password.value = "";
}
</script>