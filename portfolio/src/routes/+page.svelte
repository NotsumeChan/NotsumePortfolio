<script>
    import { writable } from 'svelte/store';

    let help = [
        "whoami - about me",
        "contact - contact me",
        "projects - list all projects",
        "skills - list all skills",
        "github - go to my github",
        "linkedin - go to my linkedin",
        "resume - download my resume",
        "clear - clear the terminal",
        "help - list all commands",
        " ",
        " "]
    let terminalContent = writable(["Welcome to the terminal", "Type help to see all commands"]);
    let historial = ["Welcome to the terminal", "Type help to see all commands"];
    let command = "";
    function executeCommand() {
        if (command == "whoami") {
            historial.push( "I'm a software developer from Chile");
        } else if (command == "contact") {
            historial.push("You can contact me at");
        }else if (command == "projects") {
            historial.push("You can see all my projects at");
        }else if (command == "skills") {
            historial.push("You can see all my skills at");
        }else if (command == "github") {
            historial.push("You can see my github at");
        }else if (command == "linkedin") {
            historial.push("You can see my linkedin at");
        }else if (command == "resume") {
            historial.push("You can download my resume at");
        }else if (command == "clear") {
            historial = [];
        }else if (command == "help") {
            for (let i = 0; i < help.length; i++) {
                historial.push(help[i]);
            }
        }else{
            historial.push("Command not found");
        }
        terminalContent.set(historial);
        command = "";
    }
</script>

<style>
    background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #262525;
        padding: 10px 30px 30px 30px;
        color: #9f4aff;
    }

    input{
        background: none;
        border: none;
        outline: none;
        color: transparent;
    }

    lines{
        display: block;
        margin-bottom: 5px;
    
    }
</style>


<background>
    {#each $terminalContent as a, b}
        <lines>{a}</lines>
    {/each}
    <form on:submit|preventDefault={executeCommand}>
        Visitor@Notsume.dev:~$
        <!-- svelte-ignore a11y-autofocus -->
        <input bind:value={command} autofocus style="color : green"/>
    </form>
</background>