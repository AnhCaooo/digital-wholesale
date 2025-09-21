import { useEffect, useState } from "react";
import type { Product } from "../../models/inventory/Product";
import type { DashboardScreenProps } from "../../models/screens/DashboardScreen";
import {
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
} from "@mui/material";

async function fetchProducts(access_token: string): Promise<Product[]> {
    const res = await fetch("http://localhost:7071/api/stocks", {
        method: "GET",
        headers: {
            // "Content-Type": "application/json",
            Authorization: access_token,
        },
    });
    if (!res.ok) {
        throw new Error(`Fetch failed: ${res.status} ${res.statusText}`);
    }

    return res.json();
}

export default function DashboardScreen({ accessToken }: DashboardScreenProps) {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        if (!accessToken) return;

        fetchProducts(accessToken)
            .then((data) => setProducts(data))
            .catch((err) => console.error("Fetch products error:", err));
    }, [accessToken]);

    return (
        <>
            <h1>Welcome back</h1>

            <TableContainer sx={{ maxHeight: 800 }}>
                <Table stickyHeader aria-label="products table">
                    <TableHead>
                        {/* First header row (grouping) */}
                        <TableRow>
                            <TableCell
                                align="center"
                                colSpan={5}
                                sx={{
                                    borderRight: "1px solid #ccc",
                                    backgroundColor: "#f5f5f5",
                                    fontWeight: "bold",
                                    fontSize: "1rem",
                                }}
                            >
                                Product
                            </TableCell>
                            <TableCell
                                align="center"
                                colSpan={2}
                                sx={{
                                    borderRight: "1px solid #ccc",
                                    backgroundColor: "#f5f5f5",
                                    fontWeight: "bold",
                                    fontSize: "1rem",
                                    maxWidth: 150, // limit total width for Color group
                                }}
                            >
                                Color
                            </TableCell>
                            <TableCell
                                align="center"
                                colSpan={2}
                                sx={{
                                    backgroundColor: "#f5f5f5",
                                    fontWeight: "bold",
                                    fontSize: "1rem",
                                    maxWidth: 200, // limit total width for Price group
                                }}
                            >
                                Price
                            </TableCell>
                        </TableRow>

                        {/* Second header row (individual columns) */}
                        <TableRow>
                            <TableCell
                                align="right"
                                sx={{ fontWeight: "bold", backgroundColor: "#fafafa" }}
                            >
                                ID
                            </TableCell>
                            <TableCell
                                sx={{ fontWeight: "bold", backgroundColor: "#fafafa" }}
                            >
                                Name
                            </TableCell>
                            <TableCell
                                align="right"
                                sx={{ fontWeight: "bold", backgroundColor: "#fafafa" }}
                            >
                                Code
                            </TableCell>
                            <TableCell
                                align="right"
                                sx={{ fontWeight: "bold", backgroundColor: "#fafafa" }}
                            >
                                EAN
                            </TableCell>
                            <TableCell
                                align="right"
                                sx={{
                                    borderRight: "1px solid #ccc",
                                    fontWeight: "bold",
                                    backgroundColor: "#fafafa",
                                }}
                            >
                                Available Stock
                            </TableCell>

                            <TableCell
                                align="right"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: "#fafafa",
                                    maxWidth: 80,
                                    whiteSpace: "nowrap",
                                    textOverflow: "ellipsis",
                                    overflow: "hidden",
                                }}
                            >
                                ID
                            </TableCell>
                            <TableCell
                                align="right"
                                sx={{
                                    borderRight: "1px solid #ccc",
                                    fontWeight: "bold",
                                    backgroundColor: "#fafafa",
                                    maxWidth: 120,
                                    whiteSpace: "nowrap",
                                    textOverflow: "ellipsis",
                                    overflow: "hidden",
                                }}
                            >
                                Value
                            </TableCell>

                            <TableCell
                                align="right"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: "#fafafa",
                                    maxWidth: 100,
                                }}
                            >
                                Wholesale
                            </TableCell>
                            <TableCell
                                align="right"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: "#fafafa",
                                    maxWidth: 100,
                                }}
                            >
                                Retail
                            </TableCell>
                        </TableRow>
                    </TableHead>

                    <TableBody>
                        {products.length === 0 ? (
                            <TableRow>
                                <TableCell colSpan={9} align="center">
                                    No products available
                                </TableCell>
                            </TableRow>
                        ) : (
                            products.map((product: Product) => (
                                <TableRow
                                    key={product.id}
                                    hover
                                >
                                    <TableCell align="right">{product.id}</TableCell>
                                    <TableCell component="th" scope="row">
                                        {product.name}
                                    </TableCell>
                                    <TableCell align="right">{product.code}</TableCell>
                                    <TableCell align="right">{product.ean}</TableCell>
                                    <TableCell
                                        align="right"
                                        sx={{ borderRight: "1px solid #ccc" }}
                                    >
                                        {product.available_stock}
                                    </TableCell>

                                    <TableCell
                                        align="right"
                                        sx={{
                                            maxWidth: 80,
                                            overflow: "hidden",
                                            textOverflow: "ellipsis",
                                        }}
                                    >
                                        {product.color.id}
                                    </TableCell>
                                    <TableCell
                                        align="right"
                                        sx={{
                                            borderRight: "1px solid #ccc",
                                            maxWidth: 120,
                                            overflow: "hidden",
                                            textOverflow: "ellipsis",
                                        }}
                                    >
                                        {product.color.value}
                                    </TableCell>

                                    <TableCell align="right" sx={{ maxWidth: 100 }}>
                                        {product.price.wholesale}
                                    </TableCell>
                                    <TableCell align="right" sx={{ maxWidth: 100 }}>
                                        {product.price.retail}
                                    </TableCell>
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
}
