# Zero-Clause BSD

# Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

def plotErrors(X, errAbs, errRel):
    """
      Plots the errors as requested by the exercise.
      The results are saved with filenames according to
      what is presented.

      Inputs:
      * X         Vector of input data.
      * errAbs    Vector of absolute errors.
      * errRel    Vector of relative errors.

    """

    import matplotlib.pyplot as plt

    # Some preparation.
    plotFuncs = [plt.plot, plt.semilogx, plt.semilogy, plt.loglog]
    errors      = [errAbs, errRel]

    errorNames    = ['Absolute', 'Relative']
    funcPlotNames    = ['standard', 'x-logarithmic', 'y-logarithmic', 'xy-logarithmic']

    # Loop over data and plot functions.
    for (error, errorName) in zip(errors, errorNames):

        for (plotFunc, plotFuncName) in zip(plotFuncs, funcPlotNames):
            fig = plt.figure()

            # Plot data points and add title.
            plotFunc(X, error, '.')
            plt.title(errorName + ' error with ' + plotFuncName + ' scaling')

            # Save plot to file.
            fig.savefig(errorName + '_' + plotFuncName + '.png')
