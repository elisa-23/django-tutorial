<template>
    <div class="left-[15%] signin">
        <h3>SIGN IN</h3>
        <form @submit.prevent="">
            <input name="email" placeholder="Enter your email" type="email" required v-model="email"></input>
            <input name="password" placeholder="Enter your password" type="password" required v-model="password"></input>
            <br>
            <button @click="signin" type="submit">Sign In</button>
        </form>
        <br>
        <p class="italic underline">Don't have an account? Click here to sign up.</p>
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
    email: email.value,
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
    console.log(token);
    userInfo.accessToken = token.access;
    userInfo.refreshToken = token.refresh;
    const user = await $fetch((config.public.apiBaseUrl + "/users/"), {
        query: {
            email: email.value,
            password: password.value,
        }
    })
    console.log(user);
}
</script>

<style scoped>

</style>