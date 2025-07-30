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

interface BaseQuestion {  //dont export, DONT NAME AS JUST QUESTION
    question: string
    quiz?: number
}

export interface Quiz {
    id: number
    title: string
    creator: number
    types: number[] | string[]
}

export type QuestionType = "multiple_choice" | "true/false" | "dropdown" | "numerical"

export interface MultipleChoiceQuestion extends BaseQuestion {
    type: "multiple_choice"
    answer: string
    incorrect: string[]
}

export interface TrueOrFalseQuestion extends BaseQuestion {
    type: "true/false"
    answer: boolean
    incorrect: boolean
}

export interface NumericalQuestion extends BaseQuestion {
    type: "numerical"
    answer: number
    incorrect: null
}

export interface DropDownQuestion extends BaseQuestion {
    type: "dropdown"
    answer: string[]
    incorrect: string[][]
}