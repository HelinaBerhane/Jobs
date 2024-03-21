import React from "react";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import { ColorSchemeScript, MantineProvider } from "@mantine/core";

import { theme } from "./theme";
import { urls } from "./urls";

import "@mantine/core/styles.css";

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
        <RouterProvider router={router} />
      </MantineProvider>
    </>
  );
}
