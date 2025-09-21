/**
 * Represents a product in the inventory
 */
export interface Product {
    id: number
    code: number
    ean: number
    name: string
    image_url: string
    color: ProductColor
    price: ProductPrice
    available_stock: number
}

/**
 * Represents product color information
 */
interface ProductColor {
    id: number
    value: string
}

/**
 * Represents product price information
 */
interface ProductPrice {
    wholesale: number
    retail: number
}