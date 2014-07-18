# -*- coding: utf-8 -*-
"""Some default configuration parameters for optimal_learning components."""
from collections import namedtuple

import moe.optimal_learning.python.python_version.optimization as python_optimization
import moe.views.constant as views_constant

# Multithreading constants
# Default number of threads to use in computation
DEFAULT_MAX_NUM_THREADS = 4
# Maximum number of threads that a user can specify
# TODO(GH-301): make this a server configurable value or set appropriate openmp env var
MAX_ALLOWED_NUM_THREADS = 10000

# Covariance constants
SQUARE_EXPONENTIAL_COVARIANCE_TYPE = 'square_exponential'

COVARIANCE_TYPES = [
        SQUARE_EXPONENTIAL_COVARIANCE_TYPE,
        ]

# GP Defaults
GaussianProcessParameters = namedtuple(
        'GaussianProcessParameters',
        [
            'length_scale',
            'signal_variance',
            ],
        )

DEFAULT_GAUSSIAN_PROCESS_PARAMETERS = GaussianProcessParameters(
    length_scale=[0.2],
    signal_variance=1.0,
    )

# Domain constants
TENSOR_PRODUCT_DOMAIN_TYPE = 'tensor_product'
SIMPLEX_INTERSECT_TENSOR_PRODUCT_DOMAIN_TYPE = 'simplex_intersect_tensor_product'

DOMAIN_TYPES = [
        TENSOR_PRODUCT_DOMAIN_TYPE,
        SIMPLEX_INTERSECT_TENSOR_PRODUCT_DOMAIN_TYPE,
        ]

# Optimizer constants
NULL_OPTIMIZER = 'null_optimizer'
NEWTON_OPTIMIZER = 'newton_optimizer'
GRADIENT_DESCENT_OPTIMIZER = 'gradient_descent_optimizer'

OPTIMIZATION_TYPES = [
        NULL_OPTIMIZER,
        NEWTON_OPTIMIZER,
        GRADIENT_DESCENT_OPTIMIZER,
        ]

# Likelihood constants
LEAVE_ONE_OUT_LOG_LIKELIHOOD = 'leave_one_out_log_likelihood'
LOG_MARGINAL_LIKELIHOOD = 'log_marginal_likelihood'

LIKELIHOOD_TYPES = [
        LEAVE_ONE_OUT_LOG_LIKELIHOOD,
        LOG_MARGINAL_LIKELIHOOD,
        ]

# EI Defaults
DEFAULT_EXPECTED_IMPROVEMENT_MC_ITERATIONS = 10000
TEST_EXPECTED_IMPROVEMENT_MC_ITERATIONS = 50

DEFAULT_OPTIMIZATION_MULTISTARTS = 200
TEST_OPTIMIZATION_MULTISTARTS = 3
PRETTY_OPTIMIZATION_MULTISTARTS = 40

DEFAULT_OPTIMIZATION_NUM_RANDOM_SAMPLES = 4000
TEST_OPTIMIZATION_NUM_RANDOM_SAMPLES = 3

# DEFAULT_NEWTON_MULTISTARTS = 200
# DEFAULT_NEWTON_PARAMETERS = python_optimization.NewtonParameters(
#         max_num_steps=100,
#         gamma=1.05,
#         time_factor=1.0e-2,
#         max_relative_change=1.0,
#         tolerance=1.0e-9,
#         )

DEFAULT_NEWTON_MULTISTARTS_MODEL_SELECTION = 200
DEFAULT_NEWTON_NUM_RANDOM_SAMPLES_MODEL_SELECTION = 0
DEFAULT_NEWTON_PARAMETERS_MODEL_SELECTION = python_optimization.NewtonParameters(
        max_num_steps=150,
        gamma=1.2,
        time_factor=5.0e-4,
        max_relative_change=1.0,
        tolerance=1.0e-9,
        )

TEST_GRADIENT_DESCENT_PARAMETERS = python_optimization.GradientDescentParameters(
        max_num_steps=5,
        max_num_restarts=2,
        num_steps_averaged=1,
        gamma=0.4,
        pre_mult=1.0,
        max_relative_change=1.0,
        tolerance=1.0e-3,
        )

DEMO_GRADIENT_DESCENT_PARAMETERS = python_optimization.GradientDescentParameters(
        max_num_steps=50,
        max_num_restarts=4,
        num_steps_averaged=0,
        gamma=0.4,
        pre_mult=1.4,
        max_relative_change=1.0,
        tolerance=1.0e-6,
        )

# DEFAULT_GRADIENT_DESCENT_MULTISTARTS = 400
# DEFAULT_GRADIENT_DESCENT_PARAMETERS = python_optimization.GradientDescentParameters(
#         max_num_steps=400,
#         max_num_restarts=10,
#         num_steps_averaged=10,
#         gamma=0.7,
#         pre_mult=0.4,
#         max_relative_change=1.0,
#         tolerance=1.0e-6,
#         )

DEFAULT_GRADIENT_DESCENT_MULTISTARTS_MODEL_SELECTION = 400
DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_MODEL_SELECTION = 0
DEFAULT_GRADIENT_DESCENT_PARAMETERS_MODEL_SELECTION = python_optimization.GradientDescentParameters(
        max_num_steps=600,
        max_num_restarts=10,
        num_steps_averaged=0,
        gamma=0.9,
        pre_mult=0.25,
        max_relative_change=0.2,
        tolerance=1.0e-5,
        )

DEFAULT_GRADIENT_DESCENT_MULTISTARTS_EI_ANALYTIC = 600
DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_EI_ANALYTIC = 10000
DEFAULT_GRADIENT_DESCENT_PARAMETERS_EI_ANALYTIC = python_optimization.GradientDescentParameters(
        max_num_steps=500,
        max_num_restarts=4,
        num_steps_averaged=0,
        gamma=0.6,
        pre_mult=1.0,
        max_relative_change=1.0,
        tolerance=1.0e-7,
        )

DEFAULT_GRADIENT_DESCENT_MULTISTARTS_EI_MC = 200
DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_EI_MC = 4000
DEFAULT_GRADIENT_DESCENT_PARAMETERS_EI_MC = python_optimization.GradientDescentParameters(
        max_num_steps=500,
        max_num_restarts=4,
        num_steps_averaged=100,
        gamma=0.6,
        pre_mult=1.0,
        max_relative_change=1.0,
        tolerance=1.0e-5,
        )

_OptimizationParameters = namedtuple('OptimizationParameters', [
    'num_multistarts',
    'num_random_samples',
    'optimization_parameters',
])

_EI_ANALYTIC_OPTIMIZER = _OptimizationParameters(
    DEFAULT_GRADIENT_DESCENT_MULTISTARTS_EI_ANALYTIC,
    DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_EI_ANALYTIC,
    DEFAULT_GRADIENT_DESCENT_PARAMETERS_EI_ANALYTIC,
)

OPTIMIZATION_TYPE_AND_OBJECTIVE_TO_DEFAULT_PARAMETERS = {
    (GRADIENT_DESCENT_OPTIMIZER, views_constant.GP_NEXT_POINTS_KRIGING_ROUTE_NAME): _EI_ANALYTIC_OPTIMIZER,
    (GRADIENT_DESCENT_OPTIMIZER, views_constant.GP_NEXT_POINTS_CONSTANT_LIAR_ROUTE_NAME): _EI_ANALYTIC_OPTIMIZER,
    (GRADIENT_DESCENT_OPTIMIZER, views_constant.GP_NEXT_POINTS_EPI_ROUTE_NAME, 'analytic'): _EI_ANALYTIC_OPTIMIZER,
    (GRADIENT_DESCENT_OPTIMIZER, views_constant.GP_NEXT_POINTS_EPI_ROUTE_NAME, 'monte_carlo'): _OptimizationParameters(
        DEFAULT_GRADIENT_DESCENT_MULTISTARTS_EI_MC,
        DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_EI_MC,
        DEFAULT_GRADIENT_DESCENT_PARAMETERS_EI_MC,
    ),
    (GRADIENT_DESCENT_OPTIMIZER, views_constant.GP_HYPER_OPT_ROUTE_NAME): _OptimizationParameters(
        DEFAULT_GRADIENT_DESCENT_MULTISTARTS_MODEL_SELECTION,
        DEFAULT_GRADIENT_DESCENT_NUM_RANDOM_SAMPLES_MODEL_SELECTION,
        DEFAULT_GRADIENT_DESCENT_PARAMETERS_MODEL_SELECTION,
    ),
    (NEWTON_OPTIMIZER, views_constant.GP_HYPER_OPT_ROUTE_NAME): _OptimizationParameters(
        DEFAULT_NEWTON_MULTISTARTS_MODEL_SELECTION,
        DEFAULT_NEWTON_NUM_RANDOM_SAMPLES_MODEL_SELECTION,
        DEFAULT_NEWTON_PARAMETERS_MODEL_SELECTION,
    ),
}

# Constant Liar constants
CONSTANT_LIAR_MIN = 'constant_liar_min'
CONSTANT_LIAR_MAX = 'constant_liar_max'
CONSTANT_LIAR_MEAN = 'constant_liar_mean'

CONSTANT_LIAR_METHODS = [
        CONSTANT_LIAR_MIN,
        CONSTANT_LIAR_MAX,
        CONSTANT_LIAR_MEAN,
        ]

DEFAULT_CONSTANT_LIAR_METHOD = CONSTANT_LIAR_MAX

# TODO(GH-257): Find a better default.
DEFAULT_CONSTANT_LIAR_LIE_NOISE_VARIANCE = 1e-12

# Kriging constants
# TODO(GH-257): Find a better default.
DEFAULT_KRIGING_NOISE_VARIANCE = 1e-8
DEFAULT_KRIGING_STD_DEVIATION_COEF = 0.0
