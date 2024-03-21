import React from "react";
import { RouteObject } from "react-router-dom";

import { HomePage } from "./Home/page";
import { HomeBage } from "./Home/bage";

export const urls: RouteObject[] = [
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/b",
    element: <HomeBage />,
  },
];
