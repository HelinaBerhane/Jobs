import React from "react";

import { RouteObject, redirect } from "react-router-dom";

import AppLayout from "./AppLayout";
import { JobsPage } from "./Jobs/JobsPage";
import { jobsApi } from "./api";

export const urls: RouteObject[] = [
  {
    path: "/",
    async loader() {
      return redirect("/jobs");
    },
  },
  {
    path: "/jobs",
    element: <AppLayout />,
    children: [
      {
        path: "/jobs",
        element: <JobsPage />,
        async loader() {
          const jobs = await jobsApi.getJobs();
          return [jobs];
        },
      },
    ],
  },
];
