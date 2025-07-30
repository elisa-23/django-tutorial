export interface User {
    id: number
    email: string
    role: string | number
    username: string
    accessToken: string
    refreshToken: string
}

export interface UserForm {
    username: string
    email: string
    password: string
}

export interface Question {
    question: string
    quiz?: number
}

export interface Quiz {
    id: number
    title: string
    creator: number
    types: number[] | string[]
}

export type QuestionType = "multipleChoice" | "trueOrFalse" | "dropDown" | "numerical"

export interface MultipleChoiceQuestion extends Question {
    type: "multipleChoice"
    answer: string
    incorrect: string[]
}

export interface TrueOrFalseQuestion extends Question {
    type: "trueOrFalse"
    answer: boolean
    incorrect: boolean
}

export interface NumericalQuestion extends Question {
    type: "numerical"
    answer: number
}

export interface DropdownQuestion extends Question {
    type: "numerical"
    answer: string[]
    incorrect: string[][]
}