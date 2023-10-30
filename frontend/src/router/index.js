import { createRouter, createWebHistory } from "vue-router";
// * Blog Pages Routes
import HomeView from "../views/blog/HomeView.vue";
import WebDevView from "../views/blog/WebDevView.vue";
import TrendsView from "../views/blog/TrendsView.vue";
import DevToolsView from "../views/blog/DevToolsView.vue";
import DiscoverView from "../views/blog/DiscoverView.vue";
import Contact from "../views/blog/Contact.vue";
import PostDetail from "../views/blog/detail/PostDetail.vue";
import CategoryDetail from "../views/blog/detail/CategoryDetail.vue";
// ! Member Routes
import Register from "../views/members/Register.vue";
import MemberLogin from "../views/members/Login.vue";
import ResetPassword from "../views/members/ResetPassword.vue";
// ! Auth
import NewPassword from "../views/members/auth/NewPassword.vue";
// ! Admin Routes
import Login from "../views/admin/Login.vue";
// ! 404
import Page404 from "../components/404/Page404.vue";
// ! Terms & Privacy
import Terms from "../views/members/terms-and-privacy/Terms.vue";
import Privacy from "../views/members/terms-and-privacy/Privacy.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/web_dev",
      name: "Web Dev",
      component: WebDevView,
    },
    {
      path: "/trends",
      name: "Trends",
      component: TrendsView,
    },
    {
      path: "/dev_tools",
      name: "Dev Tools",
      component: DevToolsView,
    },
    {
      path: "/discover",
      name: "Discover",
      component: DiscoverView,
    },
    {
      path: "/post_detail/:id",
      name: "Post Detail",
      component: PostDetail,
    },
    {
      path: "/post_detail/:category/:id",
      name: "Post Category Detail",
      component: CategoryDetail,
    },
    {
      path: "/contact",
      name: "Contact",
      component: Contact,
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
    },
    {
      path: "/login",
      name: "Login",
      component: MemberLogin,
    },
    {
      path: "/terms-and-conditions",
      name: "Terms & Conditions",
      component: Terms,
    },
    {
      path: "/privacy-policy",
      name: "Privacy Policy",
      component: Privacy,
    },
    {
      path: "/reset_password",
      name: "Reset Password",
      component: ResetPassword
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: Page404
    },
    {
      path: "/auth/new_password/member=:member_token",
      name: "New Password",
      component: NewPassword
    },
    {
      path: "/auth/login",
      name: "Admin Login",
      component: Login,
    },
  ],
});

export default router;
