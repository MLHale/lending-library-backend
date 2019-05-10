'use strict';

define('lend-database/tests/integration/components/list-pagination-test', ['qunit', 'ember-qunit', '@ember/test-helpers'], function (_qunit, _emberQunit, _testHelpers) {
  'use strict';

  (0, _qunit.module)('Integration | Component | list-pagination', function (hooks) {
    (0, _emberQunit.setupRenderingTest)(hooks);

    (0, _qunit.test)('it renders', async function (assert) {
      // Set any properties with this.set('myProperty', 'value');
      // Handle any actions with this.set('myAction', function(val) { ... });

      await (0, _testHelpers.render)(Ember.HTMLBars.template({
        "id": "e5FwRb1J",
        "block": "{\"symbols\":[],\"statements\":[[1,[21,\"list-pagination\"],false]],\"hasEval\":false}",
        "meta": {}
      }));

      assert.equal(this.element.textContent.trim(), '');

      // Template block usage:
      await (0, _testHelpers.render)(Ember.HTMLBars.template({
        "id": "f5Uu0Go3",
        "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"list-pagination\",null,null,{\"statements\":[[0,\"        template block text\\n\"]],\"parameters\":[]},null],[0,\"    \"]],\"hasEval\":false}",
        "meta": {}
      }));

      assert.equal(this.element.textContent.trim(), 'template block text');
    });
  });
});
define('lend-database/tests/lint/app.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | app');

  QUnit.test('adapters/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/application.js should pass ESLint\n\n');
  });

  QUnit.test('app.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'app.js should pass ESLint\n\n');
  });

  QUnit.test('components/list-pagination.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/list-pagination.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/application.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/cart.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/cart.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/index.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/index.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/library/index.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/library/index.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/library/library-items.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/library/library-items.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/login.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/login.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/project.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/project.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/register.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/register.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/system.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/system.js should pass ESLint\n\n');
  });

  QUnit.test('initializers/auth-manager.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/auth-manager.js should pass ESLint\n\n');
  });

  QUnit.test('initializers/navigation.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/navigation.js should pass ESLint\n\n');
  });

  QUnit.test('initializers/notification-messages.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/notification-messages.js should pass ESLint\n\n');
  });

  QUnit.test('models/category.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/category.js should pass ESLint\n\n');
  });

  QUnit.test('models/checkout.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/checkout.js should pass ESLint\n\n');
  });

  QUnit.test('models/item.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/item.js should pass ESLint\n\n');
  });

  QUnit.test('models/profile.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/profile.js should pass ESLint\n\n');
  });

  QUnit.test('models/user.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/user.js should pass ESLint\n\n');
  });

  QUnit.test('resolver.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'resolver.js should pass ESLint\n\n');
  });

  QUnit.test('router.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'router.js should pass ESLint\n\n');
  });

  QUnit.test('routes/about.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/about.js should pass ESLint\n\n');
  });

  QUnit.test('routes/cart.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/cart.js should pass ESLint\n\n');
  });

  QUnit.test('routes/checkout.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/checkout.js should pass ESLint\n\n');
  });

  QUnit.test('routes/library/index.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/library/index.js should pass ESLint\n\n');
  });

  QUnit.test('routes/library/library-items.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/library/library-items.js should pass ESLint\n\n');
  });

  QUnit.test('routes/login.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/login.js should pass ESLint\n\n');
  });

  QUnit.test('routes/register.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/register.js should pass ESLint\n\n');
  });

  QUnit.test('routes/tasks.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/tasks.js should pass ESLint\n\n');
  });

  QUnit.test('services/auth-manager.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'services/auth-manager.js should pass ESLint\n\n');
  });

  QUnit.test('services/navigation.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'services/navigation.js should pass ESLint\n\n');
  });

  QUnit.test('services/shopping-cart.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'services/shopping-cart.js should pass ESLint\n\n');
  });

  QUnit.test('storages/cart.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'storages/cart.js should pass ESLint\n\n');
  });

  QUnit.test('transitions.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'transitions.js should pass ESLint\n\n');
  });
});
define('lend-database/tests/lint/templates.template.lint-test', [], function () {
  'use strict';

  QUnit.module('TemplateLint');

  QUnit.test('lend-database/templates/about.hbs', function (assert) {
    assert.expect(1);
    assert.ok(false, 'lend-database/templates/about.hbs should pass TemplateLint.\n\nlend-database/templates/about.hbs\n  2:80  error  elements cannot have inline styles  no-inline-styles\n');
  });

  QUnit.test('lend-database/templates/application.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/application.hbs should pass TemplateLint.\n\n');
  });

  QUnit.test('lend-database/templates/cart.hbs', function (assert) {
    assert.expect(1);
    assert.ok(false, 'lend-database/templates/cart.hbs should pass TemplateLint.\n\nlend-database/templates/cart.hbs\n  49:6  error  elements cannot have inline styles  no-inline-styles\n  59:31  error  elements cannot have inline styles  no-inline-styles\n');
  });

  QUnit.test('lend-database/templates/checkout.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/checkout.hbs should pass TemplateLint.\n\n');
  });

  QUnit.test('lend-database/templates/components/list-pagination.hbs', function (assert) {
    assert.expect(1);
    assert.ok(false, 'lend-database/templates/components/list-pagination.hbs should pass TemplateLint.\n\nlend-database/templates/components/list-pagination.hbs\n  2:24  error  elements cannot have inline styles  no-inline-styles\n  3:73  error  elements cannot have inline styles  no-inline-styles\n');
  });

  QUnit.test('lend-database/templates/index.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/index.hbs should pass TemplateLint.\n\n');
  });

  QUnit.test('lend-database/templates/library/index.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/library/index.hbs should pass TemplateLint.\n\n');
  });

  QUnit.test('lend-database/templates/library/library-items.hbs', function (assert) {
    assert.expect(1);
    assert.ok(false, 'lend-database/templates/library/library-items.hbs should pass TemplateLint.\n\nlend-database/templates/library/library-items.hbs\n  6:52  error  elements cannot have inline styles  no-inline-styles\n');
  });

  QUnit.test('lend-database/templates/login.hbs', function (assert) {
    assert.expect(1);
    assert.ok(false, 'lend-database/templates/login.hbs should pass TemplateLint.\n\nlend-database/templates/login.hbs\n  8:28  error  elements cannot have inline styles  no-inline-styles\n  19:28  error  elements cannot have inline styles  no-inline-styles\n  31:79  error  elements cannot have inline styles  no-inline-styles\n');
  });

  QUnit.test('lend-database/templates/register.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/register.hbs should pass TemplateLint.\n\n');
  });

  QUnit.test('lend-database/templates/tasks.hbs', function (assert) {
    assert.expect(1);
    assert.ok(true, 'lend-database/templates/tasks.hbs should pass TemplateLint.\n\n');
  });
});
define('lend-database/tests/lint/tests.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | tests');

  QUnit.test('integration/components/list-pagination-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/list-pagination-test.js should pass ESLint\n\n');
  });

  QUnit.test('test-helper.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'test-helper.js should pass ESLint\n\n');
  });

  QUnit.test('unit/adapters/application-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/application-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/application-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/application-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/cart-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/cart-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/index-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/index-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/library/index-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/library/index-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/library/library-items-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/library/library-items-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/login-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/login-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/project-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/project-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/register-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/register-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/system-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/system-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/auth-manager-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/auth-manager-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/navigation-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/navigation-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/notification-messages-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/notification-messages-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/application-type-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/application-type-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/award-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/award-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/cart-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/cart-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/category-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/category-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/checkout-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/checkout-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/code-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/code-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/item-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/item-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/profile-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/profile-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/project-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/project-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/source-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/source-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/user-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/user-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/about-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/about-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/cart-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/cart-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/checkout-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/checkout-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/library-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/library-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/library/index-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/library/index-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/library/library-items-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/library/library-items-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/login-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/login-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/register-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/register-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/tasks-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/tasks-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/auth-manager-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/auth-manager-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/navigation-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/navigation-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/shopping-cart-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/shopping-cart-test.js should pass ESLint\n\n');
  });
});
define('lend-database/tests/test-helper', ['lend-database/app', 'lend-database/config/environment', '@ember/test-helpers', 'ember-qunit'], function (_app, _environment, _testHelpers, _emberQunit) {
  'use strict';

  (0, _testHelpers.setApplication)(_app.default.create(_environment.default.APP));

  (0, _emberQunit.start)();
});
define('lend-database/tests/unit/adapters/application-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Adapter | application', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let adapter = this.owner.lookup('adapter:application');
      assert.ok(adapter);
    });
  });
});
define('lend-database/tests/unit/controllers/application-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | application', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:application');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/cart-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | cart', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:cart');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/index-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | index', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:index');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/library/index-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | library/index', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:library/index');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/library/library-items-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | library/library-items', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:library/library-items');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/login-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | login', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:login');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/project-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | project', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:project');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/register-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | register', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:register');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/controllers/system-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Controller | system', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:system');
      assert.ok(controller);
    });
  });
});
define('lend-database/tests/unit/initializers/auth-manager-test', ['lend-database/initializers/auth-manager', 'qunit', 'ember-qunit'], function (_authManager, _qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Initializer | auth-manager', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    hooks.beforeEach(function () {
      this.TestApplication = Ember.Application.extend();
      this.TestApplication.initializer({
        name: 'initializer under test',
        initialize: _authManager.initialize
      });

      this.application = this.TestApplication.create({ autoboot: false });
    });

    hooks.afterEach(function () {
      Ember.run(this.application, 'destroy');
    });

    // Replace this with your real tests.
    (0, _qunit.test)('it works', async function (assert) {
      await this.application.boot();

      assert.ok(true);
    });
  });
});
define('lend-database/tests/unit/initializers/navigation-test', ['lend-database/initializers/navigation', 'qunit', 'ember-qunit'], function (_navigation, _qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Initializer | navigation', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    hooks.beforeEach(function () {
      this.TestApplication = Ember.Application.extend();
      this.TestApplication.initializer({
        name: 'initializer under test',
        initialize: _navigation.initialize
      });

      this.application = this.TestApplication.create({ autoboot: false });
    });

    hooks.afterEach(function () {
      Ember.run(this.application, 'destroy');
    });

    // Replace this with your real tests.
    (0, _qunit.test)('it works', async function (assert) {
      await this.application.boot();

      assert.ok(true);
    });
  });
});
define('lend-database/tests/unit/initializers/notification-messages-test', ['lend-database/initializers/notification-messages', 'qunit', 'ember-qunit'], function (_notificationMessages, _qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Initializer | notification-messages', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    hooks.beforeEach(function () {
      this.TestApplication = Ember.Application.extend();
      this.TestApplication.initializer({
        name: 'initializer under test',
        initialize: _notificationMessages.initialize
      });

      this.application = this.TestApplication.create({ autoboot: false });
    });

    hooks.afterEach(function () {
      Ember.run(this.application, 'destroy');
    });

    // Replace this with your real tests.
    (0, _qunit.test)('it works', async function (assert) {
      await this.application.boot();

      assert.ok(true);
    });
  });
});
define('lend-database/tests/unit/models/application-type-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | application type', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('application-type', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/award-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | award', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('award', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/cart-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | cart', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('cart', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/category-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | category', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('category', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/checkout-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | checkout', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('checkout', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/code-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | code', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('code', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/item-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | item', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('item', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/profile-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | profile', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('profile', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/project-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | project', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('project', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/source-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | source', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('source', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/models/user-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Model | user', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let store = this.owner.lookup('service:store');
      let model = store.createRecord('user', {});
      assert.ok(model);
    });
  });
});
define('lend-database/tests/unit/routes/about-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | about', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:about');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/cart-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | cart', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:cart');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/checkout-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | checkout', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:checkout');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/library-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | library', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:library');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/library/index-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | library/index', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:library/index');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/library/library-items-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | library/library-items', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:library/library-items');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/login-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | login', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:login');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/register-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | register', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:register');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/routes/tasks-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Route | tasks', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:tasks');
      assert.ok(route);
    });
  });
});
define('lend-database/tests/unit/services/auth-manager-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Service | auth-manager', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let service = this.owner.lookup('service:auth-manager');
      assert.ok(service);
    });
  });
});
define('lend-database/tests/unit/services/navigation-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Service | navigation', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let service = this.owner.lookup('service:navigation');
      assert.ok(service);
    });
  });
});
define('lend-database/tests/unit/services/shopping-cart-test', ['qunit', 'ember-qunit'], function (_qunit, _emberQunit) {
  'use strict';

  (0, _qunit.module)('Unit | Service | shopping-cart', function (hooks) {
    (0, _emberQunit.setupTest)(hooks);

    // Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let service = this.owner.lookup('service:shopping-cart');
      assert.ok(service);
    });
  });
});
define('lend-database/config/environment', [], function() {
  var prefix = 'lend-database';
try {
  var metaName = prefix + '/config/environment';
  var rawConfig = document.querySelector('meta[name="' + metaName + '"]').getAttribute('content');
  var config = JSON.parse(decodeURIComponent(rawConfig));

  var exports = { 'default': config };

  Object.defineProperty(exports, '__esModule', { value: true });

  return exports;
}
catch(err) {
  throw new Error('Could not read config from meta tag with name "' + metaName + '".');
}

});

require('lend-database/tests/test-helper');
EmberENV.TESTS_FILE_LOADED = true;
//# sourceMappingURL=tests.map
