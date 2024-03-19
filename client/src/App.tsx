import { useEffect, useState } from 'react';

import { BrowserRouter, Navigate, Routes, Route } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';

import LoginPage from './pages/authentication/Login.page';
import SignupPage from './pages/authentication/Signup.page';

import NavbarComponent from './components/Navbar.component';

function App() {
    const [authenticated, setAuthenticated] = useState();

    useEffect(() => {
        (async () => {
            const request = await fetch('/authenticated');
            if (request.ok) {
                setAuthenticated(await request.json());
            }
        })();
    }, []);

    return (
        <ThemeProvider theme={createTheme({
            palette: {
                mode: 'dark'
            }
        })}>
            <CssBaseline>
                <BrowserRouter>
                    {authenticated ? (
                        <>
                            <NavbarComponent />
                            <Routes>
                                <Route index />
                                <Route path='*' element={<Navigate to='/' />} />
                            </Routes>
                        </>
                    ) : (
                        <Routes>
                            <Route path='login' element={<LoginPage />} />
                            <Route path='signup' element={<SignupPage />} />
                            <Route path='*' element={<Navigate to='/login' />} />
                        </Routes>
                    )}
                </BrowserRouter>
            </CssBaseline>
        </ThemeProvider>
    );
}

export default App;
