<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
    import Navbar from '$lib/components/Navbar.svelte';
	import { ModeWatcher } from "mode-watcher";

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<ModeWatcher track={false} defaultTheme="black" defaultMode="dark" />
<Navbar />
{@render children?.()}
