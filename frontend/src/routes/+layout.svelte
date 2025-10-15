<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
    import Navbar from '$lib/components/Navbar.svelte';
	import { ModeWatcher } from "mode-watcher";
    import DialogsProvider from '$lib/dialogs/DialogsProvider.svelte';
    import { userStore } from '$lib/stores/userStore';
    import Sonner from '$lib/components/ui/sonner/sonner.svelte';

	let { children, data } = $props();
	let { userData } = data
	
	if (userData) {
		userStore.update(u => {
			return userData
		})
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<ModeWatcher track={false} defaultTheme="black" defaultMode="dark" />
<Navbar />
<Sonner richColors />
<DialogsProvider />
{@render children?.()}
