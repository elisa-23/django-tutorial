export interface User {
  email: string;
  id: number;
  role: string | number;
  username: string;
  accessToken: string;
  refreshToken: string;
}

export interface UserForm {
  email: string;
  password: string;
  username: string;
}

interface BaseQuestion {
  question: string;
  quizId: number;
}

export interface Quiz {
  id: number;
  title: string;
  creator: string;
  questions: Question[];
}

export interface MultipleChoiceQuestion extends BaseQuestion {
  question_type: "multiple choice";
  answer: string;
  incorrect: string[];
}

export interface TrueOrFalseQuestion extends BaseQuestion {
  question_type: "true/false";
  answer: boolean;
  incorrect: string[];
}

export interface NumericalQuestion extends BaseQuestion {
  question_type: "numerical";
  answer: number;
  incorrect: string[];
}

export interface DropDownQuestion extends BaseQuestion {
  question_type: "dropdown";
  answer: string[];
  incorrect: string[][];
}

export type Question =
  | MultipleChoiceQuestion
  | TrueOrFalseQuestion
  | NumericalQuestion
  | DropDownQuestion;
