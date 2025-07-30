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

export interface Question {
  question: string;
  question_type: number;
  quizId: number;
}

export interface Quiz {
  id: number;
  title: string;
  creator: string;
  questions: Question[];
}

export interface MultipleChoice extends Question {
  answer: string;
  incorrect: string[];
}

export interface TrueOrFalse extends Question {
  answer: boolean;
  incorrect: string[];
}

export interface Numeral extends Question {
  answer: number;
  incorrect: string[];
}

export interface DropDown extends Question {
  answer: string[];
  incorrect: string[][];
}
