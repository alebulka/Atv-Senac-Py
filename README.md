# @portal-dx/plugin-tech-dashboard

Welcome to the tech-dashboard plugin!

This is the backend plugin related to the tech-dashboard plugin, which presents tech metrics on the HomePage

_This plugin was created through the Backstage CLI_

## Requirements

- [Backstage](https://backstage.io/) Project;
- Node.js v18.17.1
- This plugin use Redis for data cache


## Use

Access the folder `/packages/app` and run the following command
```
yarn add @portal-dx/plugin-tech-dashboard-backend
```

In your `App-config.yaml` include this
```yaml
backend:
[...]
  cache:
    store: redis
    connection: {{ REDIS_CONNECTION }}
[...]
proxy:
  '/github-traffic-views':
    target: 'https://api.github.com/repos/madeiramadeirabr/mmrfc/traffic/views'
    changeOrigin: true
    allowedHeaders: ['Authorization', 'Accept', 'X-GitHub-Api-Version']
    allowedMethods: ['GET']
    pathRewrite:
      '^/api/proxy/github-traffic-views': ''
    headers:
      Authorization: {{ GIT_HUB_KEY }}
      Accept: 'application/vnd.github+json'
      X-GitHub-Api-Version: '2022-11-28'

  '/github-search':
    target: 'https://api.github.com/search/code'
    changeOrigin: true
    allowedMethods: ['GET']
    pathRewrite:
      '^/api/proxy/github-search/code': ''
    headers:
      Authorization: {{ GIT_HUB_KEY }}

  '/newrelic-graphql':
    target: 'https://api.newrelic.com/graphql'
    allowedMethods: [POST]
    allowedHeaders: ['X-Api-Key']
    preserveHeaderKeyCase: true
    pathRewrite:
      '^/api/proxy/newrelic-graphql': ''
    headers:
      X-Api-Key: {{ NEW_RELIC_RFC_KEY }}

  '/jira/api':
    target: https://madeiramadeira.atlassian.net
    allowedMethods: [GET]
    allowedHeaders: ['Authorization']
    headers:
      Authorization: {{ JIRA_TOKEN }}
      Accept: 'application/json'
      Content-Type: 'application/json'
[...]
 ```
In `/packages/backend/src/index.ts` create an api route

```tsx
import techDashboard from './plugins/techDashboard';
[...]
apiRouter.use('/tech-dashboard', authMiddleware, await techDashboard(techDashboardEnv));
```

In your `/packages/backend/src/plugins/` create a file `techDashboard.ts`

```tsx
import { PluginEnvironment } from '../types';
import { Router } from 'express';
import { createRouter } from '@portal-dx/plugin-tech-dashboard-backend';

export default async function createPlugin({
  logger,
  config,
}: PluginEnvironment): Promise<Router> {
  return await createRouter({
    logger,
    config,
  });
}
```
