<script lang="ts">
    import Input from "$lib/components/ui/input/input.svelte";
    import { Label } from "$lib/components/ui/label/index.js";
    import Mail from "@lucide/svelte/icons/mail";
    import Lock from "@lucide/svelte/icons/lock-keyhole";
    import Button from "$lib/components/ui/button/button.svelte";
    import { Validator } from "$lib/validator";
    import { Register } from "$lib/authFunctions";
    import { toast } from "svelte-sonner";

    let email = ""
    let password = ""
    let firstname = ""
    let lastname = ""
    let isFormValid = false

    const validator = new Validator()
    let onlyLetters = (str: string) => /^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+$/u.test(str)

    validator.addEmailField("email", () => email)
    validator.addField("password", () => password, 
        (str) => str.length >= 4)
    validator.addField("firstname", () => firstname, 
        (str) => str.length >= 3 && onlyLetters(str))
    validator.addField("lastname", () => lastname, 
        (str) => str.length >= 3  && onlyLetters(str))

    function validate() {
        isFormValid = validator.isValid()
    }
    
    async function register() {
        const res = await Register({
            email,
            password,
            firstname,
            lastname
        })

        const data = await res.json()

        if (!res.ok) {
            toast.error("Błąd podczas rejestracji", {
                description: data.error})
            return
        }
            
        window.location.reload()
    }

    const labelStyle = "row gap-2 mr-auto"
    const color = "text-gray-300"
</script>

<form oninput={validate} class="column gap-4 mt-6 w-[300px]">
    <div class="row gap-4">
        <div class="column gap-2" style="align-items: start;">
            <Label for="firstname" class="{color}">Imie</Label>
            <Input autocomplete="name" bind:value={firstname} maxlength={35} class="styled_input" id="firstname" placeholder="Jan" />
        </div>

        <div class="column gap-2" style="align-items: start;">
            <Label for="lastname" class="{color}">Nazwisko</Label>
            <Input onkeydown={(event) => /[a-z]/i.test(event.key)} autocomplete="family-name" bind:value={lastname} maxlength={35} class="styled_input" id="lastname" placeholder="Kowalski" />
        </div>
    </div>

    <div class={labelStyle}>
        <Mail class="w-4 {color}"/>
        <Label for="email2" class="{color}">Email</Label>
    </div>
    <Input autocomplete="home email" bind:value={email} maxlength={320} class="styled_input" id="email2" placeholder="twójmail@gmail.com" type="email" />

    <div class={labelStyle}>
        <Lock class="w-4 {color}" />
        <Label for="password2" class="{color}">Hasło</Label>
    </div>
    <Input autocomplete="new-password" bind:value={password} maxlength={64} class="styled_input" id="password2" placeholder="••••••••" type="password" /> 

    <Button disabled={!isFormValid} onclick={register} class="w-full mt-6 h-12 text-white">Stwórz konto</Button>
</form>