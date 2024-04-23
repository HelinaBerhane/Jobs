import React from "react";

import {
  Button,
  Group,
  Stack,
  TextInput,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { Job } from "api-client";

interface NewJobFormProps {
  onSubmit: (job: Job) => void;
}

export function NewJobForm({ onSubmit }: NewJobFormProps) {
  const form = useForm<Partial<Job>>({
    initialValues: {
      name: "",
    },
    validate: {
      name: (value) => (value ? null : "Name required"),
    },
  });

  return (
    <form
      onSubmit={form.onSubmit((values) => {
        onSubmit(values as Job);
      })}
    >
      <Stack gap="md">
        <TextInput
          label="Name"
          placeholder="Name"
          {...form.getInputProps("name")}
        />
      </Stack>

      <Group justify="flex-end" mt="md">
        <Button type="submit">Submit</Button>
      </Group>
    </form>
  );
}
