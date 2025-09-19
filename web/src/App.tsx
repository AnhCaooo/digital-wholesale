import { useState } from 'react';
import './App.css'
import { LoginScreen } from './screens/LoginScreen'
import { DashboardScreen } from './screens/DashboardScreen';

export default function App() {
  const [accessToken, setAccessToken] = useState<string>();

  if(!accessToken) {
    return <LoginScreen setAccessToken={setAccessToken} />
  }

  return (
    <>
      <DashboardScreen accessToken={accessToken}/>
    </>
  )
}

