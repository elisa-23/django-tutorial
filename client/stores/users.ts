export const useStore = defineStore('user', () => {
    const user = ref<User | null>(null)
    const isSignedIn = ref(false)
    
    async function signUp(email:string, password:string, username: string){

    }
    
    async function logIn(){
    }  

    function signOut() {
        isSignedIn.value = false
        user.value = null
      }
})