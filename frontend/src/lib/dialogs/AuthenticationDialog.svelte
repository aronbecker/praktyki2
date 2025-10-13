<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import * as Dialog from "$lib/components/ui/dialog/index.js";
    import LoginDialog from "./LoginDialog.svelte";
    import RegisterDialog from "./RegisterDialog.svelte";
    import { setDialog } from "$lib/stores/dialogStore";

    let state = $state("login");

    function toggleState() {
      state = state === "login" ? "register" : "login";
    }
</script>
 
<Dialog.Root open={true} onOpenChange={(open) => setDialog(open ? 1 : 0)}>
 <Dialog.Content class="column backdrop-blur-lg py-14">
  <Dialog.Header>
   <Dialog.Title class="text-4xl font-bold text-center">{state == "login" ? "Witaj ponownie" : "Stwórz nowe konto"}</Dialog.Title>
   <Dialog.Description class="text-center">
    Zarejestruj się lub zaloguj, aby móc korzystać <br> z pełni funkcji
   </Dialog.Description>
  </Dialog.Header>
    {#if state == "login"}
      <LoginDialog />
    {:else}
      <RegisterDialog />
    {/if}
    <Button variant="link" onclick={toggleState}>
      {state == "login" ? "Nie masz konta? Zarejestruj się" : "Masz już konto? Zaloguj się"}
    </Button>
  <Dialog.Footer>
  </Dialog.Footer>
 </Dialog.Content>
</Dialog.Root>