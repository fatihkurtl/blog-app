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
import Profile from "../views/members/auth/settings/Profile.vue";
import Customization from "../views/members/auth/settings/Customization.vue";
import Account from "../views/members/auth/settings/Account.vue";
import MemberProfile from "../views/members/auth/Profile.vue";
import ReadingList from "../views/members/auth/ReadingList.vue";
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
      path: "/web-development",
      name: "Web Dev",
      component: WebDevView,
    },
    {
      path: "/trends",
      name: "Trends",
      component: TrendsView,
    },
    {
      path: "/developer-tools",
      name: "Dev Tools",
      component: DevToolsView,
    },
    {
      path: "/discover",
      name: "Discover",
      component: DiscoverView,
    },
    {
      path: "",
      children: [
        { path: ":slug", component: PostDetail },
        { path: ":category/:slug", component: CategoryDetail },
      ],
    },
    // {
    //   path: "/:id",
    //   name: "Post Detail",
    //   component: PostDetail,
    // },
    // {
    //   path: "/:category/:id",
    //   name: "Post Category Detail",
    //   component: CategoryDetail,
    // },
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
      path: "/reset-password",
      name: "Reset Password",
      component: ResetPassword,
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: Page404,
    },
    // ! Auth
    {
      path: "/new-password/member=:member-token",
      name: "Auth New Password",
      component: NewPassword,
    },
    {
      path: "",
      children: [
        {
          path: "profile/:slug",
          name: "Auth Member Profile",
          component: MemberProfile,
        },
        {
          path: "user/:slug",
          name: "Visitor Profile",
          component: MemberProfile,
        },
      ],
    },
    // {
    //   path: "/profile/:slug",
    //   name: "Auth Member Profile",
    //   component: MemberProfile,
    // },
    {
      path: "/readinglist/member=:member-token",
      name: "Auth Member Reading List",
      component: ReadingList,
    },
    // ! Auth
    // * MEMBER SETTINGS PAGES
    {
      path: "/settings/profile/member=:member-token",
      name: "Auth Profile Settings",
      component: Profile,
    },
    {
      path: "/settings/customization/member=:member-token",
      name: "Auth Customization Settings",
      component: Customization,
    },
    {
      path: "/settings/account/member=:member-token",
      name: "Auth Account Settings",
      component: Account,
    },
    // * MEMBER SETTINGS PAGES
    {
      path: "/auth/login",
      name: "Admin Login",
      component: Login,
    },
  ],
});

export default router;
