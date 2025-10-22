<script lang="ts">
    import { dialogStore } from '$lib/stores/dialogStore';
    import AuthenticationDialog from './AuthenticationDialog.svelte';
    import EditCompanyDialog from './EditCompanyDialog.svelte';
  
    let currentDialog = $state(0)

    dialogStore.subscribe(($dialogStore) => {
        currentDialog = $dialogStore.code;
    });
</script>

{#if currentDialog == 1}
    <AuthenticationDialog />
{:else if currentDialog == 2}
    <EditCompanyDialog />
{/if}
