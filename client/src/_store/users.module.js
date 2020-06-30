import { userService } from '../_services';

const state = {
    all: {}
};

const actions = {
    getData({ commit }) {
        commit('getAllRequest');

        userService.getData()
            .then(
                data => commit('getDataSuccess', data),
                error => commit('getDataFailure', error)
            );
    },

    delete({ commit }, id) {
        commit('deleteRequest', id);

        userService.delete(id)
            .then(
                user => commit('deleteSuccess', id),
                error => commit('deleteFailure', { id, error: error.toString() })
            );
    },

    update({ commit }, userData) {
        commit('updateRequest');

        userService.update(userData)
            .then(
                response => commit('updateSuccess'),
                error => commit('updateFailure', {error: error.toString()})
            );
    }
};

const mutations = {
    getDataRequest(state) {
        state.all = { loading: true };
    },
    getDataSuccess(state, userData) {
        state.all = { userData: userData };
        //TODO: ??
    },
    getAllFailure(state, error) {
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
    }
};

export const users = {
    namespaced: true,
    state,
    actions,
    mutations
};