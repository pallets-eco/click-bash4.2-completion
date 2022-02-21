from click.shell_completion import (
    BashComplete,
    add_completion_class
)


# Only Bash >= 4.4 has the nosort option.
_SOURCE_PATCHED_BASH = """\
%(complete_func)s() {
    local IFS=$'\\n'
    local response

    response=$(env COMP_WORDS="${COMP_WORDS[*]}" COMP_CWORD=$COMP_CWORD \
%(complete_var)s=bash_complete $1)

    for completion in $response; do
        IFS=',' read type value <<< "$completion"

        if [[ $type == 'dir' ]]; then
            COMPREPLY=()
            compopt -o dirnames
        elif [[ $type == 'file' ]]; then
            COMPREPLY=()
            compopt -o default
        elif [[ $type == 'plain' ]]; then
            COMPREPLY+=($value)
        fi
    done

    return 0
}

%(complete_func)s_setup() {
    local COMPLETION_OPTIONS=""
    local BASH_VERSION_ARR=(${BASH_VERSION//./ })
    # Only BASH version 4.4 and later have the nosort option.
    if [ ${BASH_VERSION_ARR[0]} -gt 4 ] || ([ ${BASH_VERSION_ARR[0]} -eq 4 ] \
&& [ ${BASH_VERSION_ARR[1]} -ge 4 ]); then
        COMPLETION_OPTIONS="-o nosort"
    fi

    complete $COMPLETION_OPTIONS -F %(complete_func)s %(prog_name)s

}

%(complete_func)s_setup;
"""

class _PatchedBashComplete(BashComplete):
    """ Patched Shell completion for Bash """
    source_template = _SOURCE_PATCHED_BASH
    # Turn off the original version check
    def _check_version(self): pass


def patch():
    add_completion_class(_PatchedBashComplete)
