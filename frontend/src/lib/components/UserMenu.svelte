<script>
    import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
    import Button from "./ui/button/button.svelte";
    import User from '@lucide/svelte/icons/user'
    import LogOut from '@lucide/svelte/icons/log-out'
    import { Logout } from "$lib/authFunctions"

    let { firstname, lastname } = $props()
</script>

<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline" class="max-w-[145px]">
          <User />
          <p class="truncate">{firstname} {lastname}</p>
      </Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>Moje konto</DropdownMenu.Label>
      <DropdownMenu.Separator />
      <DropdownMenu.Item onSelect={Logout} class="text-red-500">
        <LogOut class="text-red-500" />
        Wyloguj
      </DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>