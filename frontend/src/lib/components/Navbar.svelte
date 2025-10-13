<script>
    import { Button } from "$lib/components/ui/button/index.js";
    import SignIn from "@lucide/svelte/icons/log-in";
    import { setDialog } from "$lib/stores/dialogStore";
</script>

<nav class="w-full h-4 row from-[#1F4067] to-[#1F4067/10] bg-linear-to-r">
    <img src="logo_skoki.png" width="80px" alt="">
    <h2 class="font-bold text-2xl">FirmaSkoki</h2>
    <Button onclick={() => setDialog(1)} class="bg-transparent ml-auto cursor-pointer" variant="outline">
        <SignIn />
        Zaloguj się
    </Button>
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
