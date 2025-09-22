# Digital Wholesale Application

## Monorepo Architecture

This project uses a **monorepo** structure, containing:

- **Frontend**: Built with [React](https://react.dev/) and [Vite](https://vitejs.dev/).
- **API Backend**: Developed using [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/) and [Python](https://www.python.org/).
- **Infrastructure**: Automated provisioning with [Terraform](https://www.terraform.io/) to deploy resources on [Azure](https://azure.microsoft.com/), including Azure Function Apps for the backend and Azure Static Web Apps for the frontend.

Each component has its own directory and dedicated README file with further setup and usage details.

---

## Objective
### Frontend
**Done:** 
- Having login screen where user can give their login code. Client code does not know (having any hardcoded value) about client code
- After login, user can see product catalog with their stock levels and pricing tailored to them. They cannot see each other
- Hosting in Azure Static Web app: Link: https://agreeable-mushroom-031698d03.2.azurestaticapps.net

**Could be better:** 
- Does not have error modal and any UI to indicate that fails to log in yet
- Does not have a switch user button, to switch user, just open new tab browser or refresh the page because credentials does not persist in web (such as storing in sessionStorage, localStorage, or any other solutions). Refresh will clear everything
- Automation tests (unit tests and e2e tests) is lacking and could be improved more

### Backend
**Done:** 
- Having a serverless API (running with Azure Function App) + Python as a language 
- Has Auth API (POST) to help user can sign in and see their own stuff based on their login code
- Has Stock API (GET) to deliver user's data related to their stocks
- How is the relationship between client and their stock/ price: each user has their own data (here we have each user has their own excel files) means that we bind client A to his data and same with client B. 
Once client A login, backend return the token to web client (now just return a plain client code, but in good practices, we should return `access_token` probably in jwt) so that web can use it to deliver correct data for specific user.

**Could be better:** 
- Does not store the data in any DB, just read data from excel file. Therefore, does not cache data as well as the operation is pretty light
- Does not yet read and serving Product Image. 
- Lacking automation tests 

### Infrastructure
**Done:** 
- Set up Azure Function App, Static Web App with Terraform 

**Could be better:** 
- Could be split ResourceGroup, StorageAccount, AppServicePlan, AzureFunctionApp and StaticWebApp into their own modules.

## Running Locally

To run the project locally, you need two terminals:

1. **Frontend**  
Navigate to the frontend directory and start the development server:
```bash
cd web
npm install
npm run dev
```
2. **Backend**  
2.1 **Locally** 

Navigate to the backend directory and start the Azure Functions host:
```bash
cd backend
# create venv
python3 -m venv .venv 
# activate it 
. .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
func start
```

When testing app locally, you might need to go and update URLs in web repo to use `localhost`, otherwise, it tries to point to API in Azure. 

2.2 **Prod**
You can also test local frontend directly, just need to run it. Because by default, it points to APIs in Azure

Refer to the respective READMEs in each directory for more information.

---

## Testing in Production

- **Frontend (Production)**: [https://agreeable-mushroom-031698d03.2.azurestaticapps.net](https://agreeable-mushroom-031698d03.2.azurestaticapps.net)
- **API (Production)**: [https://fadigitalwholesale.azurewebsites.net/api](https://fadigitalwholesale.azurewebsites.net/api)

---

## Test User
| Client Name | Client Code |
|-------------|-------------|
| Client A    | 1609        |
| Client B    | 2609        |

---

## More Information

- [Frontend README](./web/README.md)
- [Backend README](./backend/README.md)
- [Infrastructure README](./infra/README.md)