import type { DashboardScreenProps } from "../../models/DashboardScreen";

export default function DashboardScreen({accessToken}: DashboardScreenProps) {
    return (
        <>
        <h1>Dashboard screen {accessToken}</h1>
        </>
    )
}