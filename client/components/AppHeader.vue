<template>
    <div class="bg-white top-1 z-998  rounded-md left-0 flex flex-wrap justify-items-center h-screen w-fit p-5 shadow-md">
        <div class="w-[100%] h-[10%] text-center">
            <h3 v-if="signin" class="text-lg font-semibold">Welcome, {{username}}!</h3>
            <!-- create sign in button to redirect to signin page -->
            <NuxtLink to="/SignIn">
                <button v-if="!signin" class="bg-white rounded-md w-[100%] h-[50%] text-center hover:bg-[#E6E6FA] active:bg-[#CCCCFF] m-auto">Sign In</button>
            </NuxtLink>
            <button v-if="signin" class="bg-white rounded-md w-[100%] h-[50%] text-center hover:bg-[#E6E6FA] active:bg-[#CCCCFF] m-auto" @click="userStore.signOut">
                Sign Out
            </button>
        </div>
    </div>
</template>

<script setup>
const userStore = useUserStore();
const signin = computed(() => userStore.isSignedIn);
const username = computed(() => userStore.userInfo.username);

</script>