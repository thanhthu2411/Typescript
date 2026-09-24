import type { HasFormatter } from "../interfaces/HasFormatter.js"

export class Payment implements HasFormatter {
    // readonly client: string
    // public details: string
    // private amount: number

    // constructor(c: string, d: string, a: number) {
    //     this.client = c
    //     this.details = d
    //     this.amount = a
    // }

    constructor(
        readonly recipient: string,
        public details: string,
        private amount: number
    ) {}

    format() {
        return `${this.recipient} is owed $${this.amount} for ${this.details}`
    }
}





