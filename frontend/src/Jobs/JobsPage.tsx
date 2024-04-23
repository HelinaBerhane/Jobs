import React, { useContext, useEffect } from "react";
import { useLoaderData, useRevalidator } from "react-router-dom";

import { Stack } from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { Job } from "api-client";

import { AppControlContext } from "../AppLayout";
import { jobsApi } from "../api";
import { ResponsiveModal } from "../components/ResponsiveModal";
import { NewJobForm } from "./NewJobForm";
import { JobsTable } from "./JobsTable";

export function JobsPage() {
  const [
    newJobDisclosure,
    { toggle: toggleNewJobDisclosure, close: closeNewJobDisclosure },
  ] = useDisclosure();

  const [jobs] = useLoaderData() as [
    Job[],
  ];
  const { revalidate } = useRevalidator();

  const appControls = useContext(AppControlContext);

  useEffect(() => {
    appControls.setTitle("Jobs");
    appControls.setLeadingAction({
      type: "none",
    });
    appControls.setTrailingAction({
      type: "button",
      id: "new-job",
      variant: "filled",
      content: "New job",
    });
    appControls.onAction((actionId) => {
      switch (actionId) {
        case "new-job":
          return toggleNewJobDisclosure();
        default:
          return;
      }
    });
  }, []);

  return (
    <Stack>
      <JobsTable onDelete={async (id) => {
            await jobsApi.deleteJob({ jobId: id });
            revalidate();
          }} 
          jobs={jobs}/>

      <ResponsiveModal
        onClose={closeNewJobDisclosure}
        opened={newJobDisclosure}
        title="Add job"
      >
        <NewJobForm
          onSubmit={async (newJob) => {
            await jobsApi.createJob({ job: newJob });
            closeNewJobDisclosure();
            revalidate();
          }}
        />
      </ResponsiveModal>
    </Stack>
  );
}
