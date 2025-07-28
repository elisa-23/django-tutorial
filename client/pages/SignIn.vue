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
async function signin() {
    const token = await fetchEndpoint<{ access: string, refresh: string }>("/api/token/", 'POST', {
        email: email.value, // or username //make sure the field name is the same as dj
        password: password.value,
    });          
    if (!token || !token.access || !token.refresh) {
        alert("Invalid email or password. Please try again.");
        return;
    }

    userInfo.accessToken = token.access;
    userInfo.refreshToken = token.refresh;

    const base64Url = (userInfo.accessToken.split('.')[1]) || "";
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

    let decodedPayLoad = {user_id: 0};
    decodedPayLoad = JSON.parse(window.atob(base64));

    interface BasicInfo {
        email: string
        role: string
        username: string
    }
    const user = await fetchEndpoint<BasicInfo[]>('/users/', 'GET', undefined, {
        id: decodedPayLoad.user_id,
    });

    userInfo.id = decodedPayLoad.user_id;
    if (user.length > 0) {
        userInfo.role = user[0]?.role || "";
        userInfo.username = user[0]?.username || "";
        userInfo.email = user[0]?.email || "";
    } else {
        alert(`User NOT found. There is no user with this ID: ${decodedPayLoad.user_id}`)
    }
    email.value = "";
    password.value = "";
    console.log(userInfo)
}
</script>