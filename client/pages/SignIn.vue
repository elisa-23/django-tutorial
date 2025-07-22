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
        <NuxtLink to="/SignUp">
            <p class="italic underline hover:text-sky-600">Don't have an account? Click here to sign up.</p>
        </NuxtLink>
    </div>
</template>

<script setup lang="ts">

const email = ref('');
const password = ref('');

const config = useRuntimeConfig();       // base url access = config.public.apiBase

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

async function signin() {
    let token = {
        access: "",
        refresh: "",
    }
    token = await $fetch((config.public.apiBaseUrl + "/api/token/"), { 
        method: 'POST',
        body: {
            email: email.value, // or username //make sure the field name is the same as dj
            password: password.value,
        },
    });
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

    let user: BasicInfo[] = ([
        {
            email: "",
            role: "",
            username: ""
        }
    ])
    user = (await $fetch((config.public.apiBaseUrl + "/users/"), {
        params: {
            id: decodedPayLoad.user_id,
        }
    }))
    console.log(user);
    userInfo.id = decodedPayLoad.user_id;
    if (user.length > 0) {
        userInfo.role = user[0]?.role || "";
        userInfo.username = user[0]?.username || "";
        userInfo.email = user[0]?.email || "";
    } else {
        alert(`User NOT found. There is no user with this ID: ${decodedPayLoad.user_id}`)
    }
    console.log(userInfo);
    email.value = "";
    password.value = "";
}
</script>