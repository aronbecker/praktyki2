<script lang="ts">
    import { Button } from "$lib/components/ui/button/index.js";
    import SignIn from "@lucide/svelte/icons/log-in";
    import { setDialog } from "$lib/stores/dialogStore";
    import { userStore } from "$lib/stores/userStore";
    import type { UserData } from "$lib/stores/userStore";
    import UserMenu from "./UserMenu.svelte";

    let userData: UserData | null = null
    userStore.subscribe(ud => userData = ud)
</script>

<nav class="w-full h-4 row from-[#1F4067] to-[#1F4067/10] bg-linear-to-r">
    <img src="/logo_skoki.png" width="80px" alt="">
    <a href="/" class="font-bold text-2xl mr-auto">FirmaSkoki</a>
    {#if userData}
        <UserMenu firstname={userData.firstname} lastname={userData.lastname}/>
    {:else}
        <Button onclick={() => setDialog({code: 1})} class="bg-transparent cursor-pointer" variant="outline">
            <SignIn />
            Zaloguj się
        </Button>
    {/if}
</nav>

<style>
    nav {
        padding: 3rem 1rem 5rem 0rem;
    }
    
    @media only screen and (min-width: 600px) {
        nav {
            padding: 3rem 2rem;
        }
    }
</style>
