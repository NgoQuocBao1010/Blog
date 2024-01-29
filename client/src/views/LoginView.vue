<script setup>
import InputGroup from "primevue/inputgroup";
import InputGroupAddon from "primevue/inputgroupaddon";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import { ref } from "vue";

const email = ref("");
const password = ref("");
</script>

<template>
    <div class="login-container">
        <div class="input-container">
            <label for="username">Username</label>
            <InputText
                id="username"
                v-model="email"
                aria-describedby="username-help"
            />
        </div>

        <div class="input-container">
            <label for="password">Password</label>
            <InputText
                id="password"
                v-model="password"
                aria-describedby="password-help"
            />
        </div>

        <Button label="Submit" />
    </div>
</template>

<style lang="scss" scoped>
.login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    aspect-ratio: 2 / 1;
    width: 35%;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    padding: 1rem 2rem;

    .input-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 1rem;

        input {
            width: 20rem;
        }
    }
}
</style>
