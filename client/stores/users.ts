export const useUserStore = defineStore('user', () => {
    const isSignedIn = ref(false);
    const userInfo = ref<User>();
    const accessToken = ref('');
    const refreshToken = ref('');
    async function signIn(email: string, password: string) {
        const token = await fetchEndpoint<{ access: string, refresh: string }>("/api/token/", 'POST', {
            email: email, // or username //make sure the field name is the same as dj
            password: password,
        });
        if (!token) {
            alert("Invalid email or password. Please try again.");
            return;
        }

        accessToken.value = token.access;
        refreshToken.value = token.refresh;

        const base64Url = (accessToken.value.split('.')[1]) || "";
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

        let decodedPayLoad = JSON.parse(window.atob(base64));

        interface BasicInfo {
            email: string
            role: string
            username: string
        }
        const user = await fetchEndpoint<BasicInfo[]>('/users/', 'GET', undefined, {
            id: decodedPayLoad.user_id,
        });
        if (!user) {
            alert("Failed to fetch user information. Please try again.");
            return;
        }
        console.log("User fetched:", user);

        userInfo.value.id = decodedPayLoad.user_id;
        if (user.length > 0) {
            userInfo.value.role = user[0]?.role || "";
            userInfo.value.username = user[0]?.username || "";
            userInfo.value.email = user[0]?.email || "";
        } else {
            alert(`User NOT found. There is no user with this ID: ${decodedPayLoad.user_id}`)
        }
        isSignedIn.value = true;
    }
    async function signUp(email: string, password: string, username: string, role: number) {
        const createdUser = await fetchEndpoint<User>('/users/', 'POST', {
            email: email,
            username: username,
            password: password,
            role: role,
        });
        if (!createdUser) {
            alert("Failed to create user. Please try again.");
            return;
        }
        await signIn(email, password);
    }
    async function signOut() {
        isSignedIn.value = false;
        userInfo.value = { email: '', id: 0, role: '', username: '', accessToken: '', refreshToken: '' };
        // Optionally, you can also blacklist the refresh token on the server
        const token = userInfo.value?.refreshToken;
        if (token) {
            await fetchEndpoint('/api/token/blacklist/', 'POST', { refresh: token });
        }
    }
    return { isSignedIn, userInfo, accessToken, refreshToken, signIn, signUp, signOut };
})