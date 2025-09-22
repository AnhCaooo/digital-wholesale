# Digital Wholesale UI

An UI application built with React 19 + Vite.

## Tech Stack:

- Frontend framework: [React](https://react.dev/)
- Building tool: [Vite](https://vite.dev/)
- Unit test: [Vitest](https://vitest.dev/)
- Design System: [Material UI](https://mui.com)

## Getting started

To run the project locally:

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The app will be available at [http://localhost:5173](http://localhost:5173) by default.

3. There is 2 test users with these credentials: 
- Client A - client code: 1609
- Client B - client code: 2309

## Deploy to Azure 
```bash 
swa build 

swa deploy ./dist --app-name <swa_name> --env default --deployment-token <deploytoken_get_from_terraform_output>
```

## Out of scope:
Due to this is not a PROD application, some following factors are ignored:  
1. Credentials do not persist in web application which means after login, user closes the tab, then they need to login again. 
2. UI components should be handle more graceful.
3. Handle error cases such as: 
    - fails to login should show dialog to indicate user what went wrong 
    - fails to fetch products  
4. Automation tests (unit tests and e2e tests) will be lacking