import React from "react";

import { Button, Table } from "@mantine/core";

import { Job } from "api-client";

export interface JobsTableProps {
  jobs: Job[];
  onDelete: (jobId: string) => void;
}

export function JobsTable({ jobs, onDelete }: JobsTableProps) {
  const rows = jobs.map((job) => {
    return (
      <Table.Tr key={job.id}>
        <Table.Td>{job.name}</Table.Td>
        <Table.Td>
          <Button onClick={() => onDelete(job.id!)} size="xs" variant="danger">
            Delete
          </Button>
        </Table.Td>
      </Table.Tr>
    );
  });

  return (
    <Table>
      <Table.Thead>
        <Table.Tr>
          <Table.Th>Name</Table.Th>
          <Table.Th>Delete</Table.Th>
        </Table.Tr>
      </Table.Thead>
      <Table.Tbody>{rows}</Table.Tbody>
    </Table>
  );
}
