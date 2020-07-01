import { userService } from '../_services';

const state = {
    all: {
        items: {},
        matches: {},
    },
};

const actions = {
    getData({ commit }) {
        commit('getDataRequest');

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

    getAll({ commit, state}) {
        userService.getAll()
            .then(
                response => commit('getAllSuccess', response),
                error => commit('getAllFailure', {error: error.toString()})

            )
    },

    getMatches({ commit, state }){
        userService.getMatches()
            .then(
                response => commit('getMatchesSuccess', response),
                error => commit('getMatchesFailure', {error: error.toString()})
            )
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
    getAllSuccess(state, users) {
        state.all.items = users;
    },
    getAllFailure(state, error) {

    },
    getMatchesSuccess(state, users) {
        state.all.matches = users;
    },
    getMatchesFailure(state, error) {

    },
};

export const users = {
    namespaced: true,
    state,
    actions,
    mutations
};