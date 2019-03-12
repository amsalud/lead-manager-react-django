import { CREATE_MESSAGE } from './types';

// CREATE MESSSAGE
export const createMessage = msg => {
    return {
        type: CREATE_MESSAGE,
        payload: msg
    }
}