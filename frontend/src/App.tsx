import React from "react";

import { SafeArea } from "capacitor-plugin-safe-area";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import { ColorSchemeScript, MantineProvider } from "@mantine/core";
import { Notifications } from "@mantine/notifications";
import { NavigationProgress } from "@mantine/nprogress";

import { theme } from "./theme";
import { urls } from "./urls";

import "@mantine/core/styles.css";
import "@mantine/notifications/styles.css";
import "@mantine/nprogress/styles.css";

SafeArea.getSafeAreaInsets().then(({ insets }) => {
  document.documentElement.style.setProperty("--inset-top", insets.top + "px");
  document.documentElement.style.setProperty(
    "--inset-bottom",
    insets.bottom + "px"
  );
});

const router = createBrowserRouter(urls);

export default function App() {
  return (
    // Note: typically lowercase imports are divs and Uppercase imports are functions */}
    // these are called composit vs host components */}
    <>
      {/* ColorSchemeScript sets the colour scheme before hydration to avoid a flash of inaccurate color scheme in server side rendered applications */}
      <ColorSchemeScript />
      <MantineProvider
        // MantineProvider sets the context that the mantine themes should be used throughout the app, instead of prop drilling
        defaultColorScheme="auto"
        theme={theme}
      >
        {/* @ts-expect-error - style prop is supported by <NavigationProgress />, but types are incorrect */}
        <NavigationProgress style={{ top: "var(--inset-top)" }} />
        <div
          style={{
            backgroundColor: "var(--mantine-color-body)",
            height: "var(--inset-top)",
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            zIndex: 99999,
          }}
        />
        <div
          style={{
            backgroundColor: "var(--mantine-color-body)",
            height: "var(--inset-bottom)",
            position: "fixed",
            bottom: 0,
            left: 0,
            right: 0,
            zIndex: 99999,
          }}
        />
        <Notifications />
        <RouterProvider router={router} />
      </MantineProvider>
    </>
  );
}
