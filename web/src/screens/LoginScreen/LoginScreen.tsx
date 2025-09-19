import "./LoginScreen.css";

import { useMemo, useState } from "react";
import {
    Box,
    Button,
    Container,
    TextField,
    Typography,
    Paper,
} from "@mui/material";

export default function LoginScreen() {
    const [clientCode, setClientCode] = useState("");

    // Memo that returns true if clientCode is having string
    const hasError = useMemo(() => clientCode.length > 0 && isNaN(Number(clientCode)), [clientCode]);

    // Memo that returns a helper message if clientCode contains string
    const getHelperText = useMemo(
        () => (clientCode.length > 0 && isNaN(Number(clientCode)) ? "Code is not right format" : ""),
        [clientCode]
    );

    // Handle when user clicks on submit button
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("Client code:", clientCode);
        // Send auth request to backend to authenticate and authorize user
        // After get response, navigate them to dashboard screen
    };

    return (
        <Container maxWidth="sm">
            <Paper
                elevation={4}
                sx={{
                    p: 4,
                    mt: 8,
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    borderRadius: 3,
                }}
            >
                {/* Header title */}
                <Typography variant="h4" component="h1" gutterBottom>
                    Digital Wholesale
                </Typography>

                {/* Input field for client's code */}
                <Box
                    component="form"
                    onSubmit={handleSubmit}
                    sx={{ mt: 2, width: "100%" }}
                    autoComplete="off"
                >
                    <TextField
                        required
                        fullWidth
                        label="Client Code"
                        variant="outlined"
                        value={clientCode}
                        onChange={(e) => setClientCode(e.target.value)}
                        margin="normal"
                        error={hasError}
                        helperText={getHelperText}
                    />

                    {/* Submit button */}
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 2, py: 1.5 }}
                    >
                        Login
                    </Button>
                </Box>
            </Paper>
        </Container>
    );
}
