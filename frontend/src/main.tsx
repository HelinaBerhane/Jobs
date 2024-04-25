import React, { StrictMode } from "react";

import { createRoot } from "react-dom/client";

import App from "./App";

const root = createRoot(document.getElementById("root")!);
root.render(
    // Note: <StrictMode> helps to find common bugs in components early during development.
    // See https://react.dev/reference/react/StrictMode
    <StrictMode>
        <App />
    </StrictMode>
);