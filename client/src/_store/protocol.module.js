import { protocolService } from '../_services';
import { secretsService } from '../_services';
import { apiService } from '../_services';

const state = {
    protocols: {}
};

const actions = {
    getProtocols( {dispatch, commit }) {
        return apiService.protocols();
    }
};

const mutations = {
    getDataRequest(state) {
        state.all = { loading: true };
    },
    getDataSuccess(state, users) {
        // state.all = { items: users };
        //TODO: ??
    },
    getDataFailure(state, error) {
        state.all = { error };
    },
    deleteRequest(state, id) {
        // add 'deleting:true' property to user being deleted
        state.all.items = state.all.items.map(user =>
            user.id === id
                ? { ...user, deleting: true }
                : user
        )
    },
    deleteSuccess(state, id) {
        // remove deleted user from state
        state.all.items = state.all.items.filter(user => user.id !== id)
    },
    deleteFailure(state, { id, error }) {
        // remove 'deleting:true' property and add 'deleteError:[error]' property to user 
        state.all.items = state.items.map(user => {
            if (user.id === id) {
                // make copy of user without 'deleting:true' property
                const { deleting, ...userCopy } = user;
                // return copy of user with 'deleteError:[error]' property
                return { ...userCopy, deleteError: error };
            }

            return user;
        })
    },
    updateRequest(state) {
        state.all = { loading: true };
    },
    updateSuccess(state) {
        state.all = { loading: false};
    },
    updateFailure(state, error) {
        state.all = { loading: false}; //TODO: handle the error message
    },
    getAllSuccess(state, users) {
        state.all = { items: users };
    },
    getAllFailure(state, error) {

    },
};

export const protocol = {
    namespaced: true,
    state,
    actions,
    mutations
};