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

<script setup>

const email = ref('');
const password = ref('');

onBeforeMount(() => {
    email.value = '';
    password.value = '';
})

function signin() {
    const config = useRuntimeConfig();       // base url access = config.public.apiBase
}
</script>

<style scoped>

</style>