<script>
    import Input from "$lib/components/ui/input/input.svelte";
    import { Label } from "$lib/components/ui/label/index.js";
    import Mail from "@lucide/svelte/icons/mail";
    import Lock from "@lucide/svelte/icons/lock-keyhole";
    import Button from "$lib/components/ui/button/button.svelte";
    import { Validator } from "$lib/validator";

    let email = ""
    let password = ""
    let isFormValid = false

    const validator = new Validator()

    validator.addEmailField("email", () => email)
    validator.addField("password", () => password, (str) => str.length >= 4)

    function validate() {
        isFormValid = validator.isValid()
    }

    function signIn() {
        alert("Zalogowano");
    }

    const labelStyle = "row gap-2 mr-auto"
    const color = "text-gray-300"
</script>

<form oninput={validate} class="column gap-4 mt-6 w-[300px]">
    <div class={labelStyle}>
        <Mail class="w-4 {color}"/>
        <Label for="email" class="{color}">Email</Label>
    </div>
    <Input autocomplete="email" bind:value={email} maxlength={320} class="styled_input" id="email" placeholder="twójmail@gmail.com" type="email" />
    <div class={labelStyle}>
        <Lock class="w-4 {color}" />
        <Label for="password" class="{color}">Hasło</Label>
    </div>
    <Input autocomplete="current-password" bind:value={password} maxlength={64} class="styled_input" id="password" placeholder="••••••••" type="password" />
    <Button disabled={!isFormValid} onclick={signIn} class="w-full mt-6 h-12 text-white">Zaloguj się</Button>
</form>