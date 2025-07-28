export const useUserStore = defineStore('user', {
    state: () => ({
        isSignedIn: false,
        userInfo: null as User | null
    }),
    actions: {
        async signIn(email: string, password: string, userInfo: User) {
            const token = await fetchEndpoint<{ access: string, refresh: string }>("/api/token/", 'POST', {
                email: email, // or username //make sure the field name is the same as dj
                password: password,
            });
            if (!token || !token.access || !token.refresh) {
                alert("Invalid email or password. Please try again.");
                return;
            }

            userInfo.accessToken = token.access;
            userInfo.refreshToken = token.refresh;

            const base64Url = (userInfo.accessToken.split('.')[1]) || "";
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

            let decodedPayLoad = { user_id: 0 };
            decodedPayLoad = JSON.parse(window.atob(base64));

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

            userInfo.id = decodedPayLoad.user_id;
            if (user.length > 0) {
                userInfo.role = user[0]?.role || "";
                userInfo.username = user[0]?.username || "";
                userInfo.email = user[0]?.email || "";
            } else {
                alert(`User NOT found. There is no user with this ID: ${decodedPayLoad.user_id}`)
            }
            this.userInfo = userInfo;
            this.isSignedIn = true;
        },
        async signUp(email: string, password: string, username: string, role: number) {
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
            await this.signIn(email, password, createdUser);
        },
        async signOut() {
            this.isSignedIn = false;
            this.userInfo = null;
        }
    }
})