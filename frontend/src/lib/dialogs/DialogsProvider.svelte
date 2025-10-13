<script lang="ts">
    import { dialogStore } from '$lib/stores/dialogStore';
    import AuthenticationDialog from './AuthenticationDialog.svelte';
  
    let currentDialog = $state(0)

    dialogStore.subscribe(($dialogStore) => {
        currentDialog = $dialogStore;
    });
</script>

{#if currentDialog == 1}
    <AuthenticationDialog />
{/if}