import { describe, expect, test } from 'vitest'
import { LoginScreen } from '../../screens/LoginScreen'
import { render, screen } from "@testing-library/react";

describe("LoginScreen", () => {
    test('renders', async () => {
        render(<LoginScreen />)
        const headerTitle = screen.getByRole('heading', {level: 1})
        expect(headerTitle).toBeDefined()
    })
})
