import { Configuration, DefaultApi } from "api-client";

export const jobsApi = new DefaultApi(
  new Configuration({
    basePath: "http://0.0.0.0:8000",
  })
);
